const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');
html = html.split('\\\\n').join('');
fs.writeFileSync('index.html', html, 'utf-8');
console.log('Fixed backslash-n');
