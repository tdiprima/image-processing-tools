/*
Fetches data from a given URL, processes it (assuming it's in CSV format), converts
the data into a PNG image, and renders it on an HTML canvas element.

TODO: Ensure a CSV file exists and is hosted on a server or accessible via a public URL.
 The first line of the file should contain metadata (e.g., image dimensions), and subsequent lines should contain pixel data (x, y, R, G, B).
 Call the getDataForImage(url) function from the browser's developer console.
 getDataForImage('https://example.com/path/to/data.csv');
*/
fetch_data = function (url) {
    return fetch(url).then((response) => {
        if (response.ok) {
            return response.text(); // Always fetch as text first
        } else {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    }).then((text) => {
        try {
            console.log('Fetched content:', text); // Debugging output

            // Try parsing the first line as JSON
            const lines = text.split(/\r?\n/);
            JSON.parse(lines[0]); // Check if first line is valid JSON
            return text; // Return the raw text if parsing succeeds
        } catch (err) {
            throw new Error(`Invalid JSON in the first line: ${err.message}`);
        }
    });
};


getDataForImage = function (url) {
    fetch_data(url)
        .then((response) => csv2png(response, ','))
        .then((dataUri) => {
            console.log('Image generated:', dataUri);
        })
        .catch((err) => {
            console.error('Error processing data:', err);
        });
};


csv2png = function (strData, strDelimiter) {
  strDelimiter = (strDelimiter || ",");

  let lines = strData.split(/\r?\n/); // split by newline

  // Do something with headers at some point
  let headers = lines[1];

  let str = lines[0];
  str = str.replace(/['""]+/g, '"'); // double quotes
  str = str.replace(/['"]+/, ''); // starts with quote
  str = str.replace("}\"", "}");
  // str = str.replace("\",,,,", ""); // ends with quote and commas
  if (str.endsWith(",,,,")) {
    str = str.replace(",,,,", "");
  }
  if (str.endsWith(",,,")) {
    str = str.replace(",,,", "");
  }
  console.log(str);

  const metadata = JSON.parse(str);

  // let width = parseInt(metadata.img_width),
  //     height = parseInt(metadata.img_height);
  width = parseInt(metadata.png_w);
  height = parseInt(metadata.png_h);
  console.log('size of buffer', width * height * 4);// = imgData.data.length

  // create off-screen canvas element
  let canvas = document.getElementById("myCanvas");

  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'myCanvas';
  }
  canvas.width = width;
  canvas.height = height;
  let ctx = canvas.getContext("2d");
  imgData = ctx.createImageData(width, height);
  let i;

  // Initialize buffer to white with transparency
  for (i = 0; i < imgData.data.length; i += 4) {
    imgData.data[i] = 255;
    imgData.data[i + 1] = 255;
    imgData.data[i + 2] = 255;
    imgData.data[i + 3] = 255;
  }

  // Data from CSV file
  for (i = 2; i < lines.length; i++) {

    // Ignore if blank line
    if (lines[i].trim().length > 0) {

      let line = lines[i].split(strDelimiter);
      let x = parseInt(line[0]);
      let y = parseInt(line[1]);
      // let pixelindex = (x * width + y) * 4; <-- Tahsin make-it-fit modification
      let pixelindex = (y * width + x) * 4;

      // Color
      imgData.data[pixelindex] = parseInt(line[2]);      // R value [0, 255]
      imgData.data[pixelindex + 1] = parseInt(line[3]);  // G value
      imgData.data[pixelindex + 2] = parseInt(line[4]);  // B value
      imgData.data[pixelindex + 3] = 255;                // set alpha channel
    }
  }
  ctx.putImageData(imgData, 0, 0); // we now have an image painted to the canvas
  // document.body.append(canvas);

  // Next, create an image file:
  let dataUri = canvas.toDataURL(); // produces a PNG file

  return dataUri;
};
