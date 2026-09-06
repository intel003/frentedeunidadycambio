const fs = require('fs');

const instagramEmbed = '<div class="video-container transform transition duration-500 hover:scale-[1.02]" style="background: linear-gradient(45deg, #38b6ff, #00bf63); padding: 4px; border-radius: 1rem; box-shadow: 0 10px 30px -5px rgba(56, 182, 255, 0.4), 0 10px 30px -5px rgba(0, 191, 99, 0.4); max-width: 400px; margin: 0 auto;">\\n' +
'                <div class="video-inner overflow-hidden relative bg-white" style="border-radius: 0.8rem; aspect-ratio: 9/16; display: flex; align-items: center; justify-content: center;">\\n' +
'                    <iframe src="https://www.instagram.com/reel/Dc1_Fh0Odj8/embed" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" allowfullscreen="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>\\n' +
'                </div>\\n' +
'            </div>';

let indexHtml = fs.readFileSync('index.html', 'utf-8');

const searchRegex = /<div class="video-container transform transition duration-500 hover:scale-\[1\.02\]">[\s\S]*?<\/div>\s*<\/section>/;

if (indexHtml.match(searchRegex)) {
    indexHtml = indexHtml.replace(searchRegex, instagramEmbed + '\\n          </section>');
    fs.writeFileSync('index.html', indexHtml, 'utf-8');
    console.log('Replaced local video with Instagram embed in index.html');
} else {
    console.log('Could not find the video container to replace.');
}
