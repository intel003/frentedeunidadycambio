const fs = require('fs');

let indexHtml = fs.readFileSync('index.html', 'utf-8');

// The literal \\n needs to be removed
indexHtml = indexHtml.replace(/>\\\\n/g, '>');
indexHtml = indexHtml.replace(/\\\\n</g, '<');
// Just in case it's floating as a text node:
indexHtml = indexHtml.replace(/\\\\n/g, '');

fs.writeFileSync('index.html', indexHtml, 'utf-8');
console.log('Fixed \\n issue');
