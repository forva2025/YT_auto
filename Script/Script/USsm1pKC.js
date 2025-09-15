// Import required packages
const fs = require('fs'); // For reading files
const puppeteer = require('puppeteer-core'); // For browser automation
const url = 'https://studio.youtube.com/'; // URL to navigate to
const delayRandom = require('delay-random'); // For adding random delays

// Read the upload text that was created previously
fs.readFile('upload_text.txt', 'utf8', function(err, data) {
    if (err) throw err; // Show if something is wrong with the file
    lines = data.split('\n'); // Split the file into individual lines
});

//  https://cracked.io/Evil-Corporation Launch Puppeteer browser instance with a local cache storage
puppeteer.launch({
  userDataDir: './uploader_cache', // The location where the cache will be stored
  executablePath: require('puppeteer').executablePath(), // Path to the executable of a specific version of Chrome (installed by Puppeteer)
  headless: false, // Run the browser in GUI mode
  args: ['--no-sandbox'] // Arguments to pass to the browser
})
.then(async browser => {
	const page = await browser.newPage(); // Open a new page
	await page.setCacheEnabled(true); // Enable the cache to save the sessions
	await page.setViewport({ width: 1280, height: 720 }); // Set the size for the browser window
	// Read the cookies from a JSON file
	const cookies = JSON.parse(fs.readFileSync('cookies.json', 'utf8'));
	// Add the cookies to the page
	for (const cookie of cookies) {
	await page.setCookie(cookie);
	}
	await page.goto(url); // Go to the YouTube Studio website
	await delayRandom(14000, 26000); // Wait for the website to load (adjust based on your internet speed)
	// From this point on, the script interacts with the website by clicking buttons and entering text
	await page.click('#create-icon'); // Click on the 'Create' button
	await delayRandom(1000, 2000); // Wait for the next step to load
	await page.click('#text-item-0'); // Click on the 'Text' option
	await delayRandom(1000, 2000); // Wait for the next step to load
	await page.click('#select-files-button'); // Click on the 'Select files' button
	await delayRandom(1000, 2000); // Wait for the next step to load
	const elementHandle = await page.$("input[type=file]"); // Get the file input element
	await elementHandle.uploadFile('clip.mp4'); // Upload the video file (make sure everything is in the same folder)
	await delayRandom(8000, 10000); // Wait for the file to upload (adjust based on your file size)
	await page.keyboard.type(lines[0], {delay: 150}); // Enter the title of the video
	await delayRandom(1000, 2000); // Wait for the next step to load https://cracked.io/Evil-Corporation
	await page.keyboard.press('Tab'); // Move to the next input field
	await delayRandom(500, 600); // Wait for the next step to load
	await page.keyboard.press('Tab'); // Move to the next input field
	await delayRandom(1000, 2000); // Wait for the next step to load
	await page.focus('#description-container'); //focus on the description container
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.type(lines[1], {delay: 150}); //type the first line of the description with a delay between keystrokes
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.type(lines[2], {delay: 150}); //type the second line of the description with a delay between keystrokes
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.click('#audience > ytkc-made-for-kids-select > div.made-for-kids-rating-container.style-scope.ytkc-made-for-kids-select > tp-yt-paper-radio-group > tp-yt-paper-radio-button:nth-child(2)'); //click the "No, it's not made for kids" radio button
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.press('Tab'); //press the Tab key https://cracked.io/Evil-Corporation
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.press('Tab'); //press the Tab key again
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.press('Enter'); //press the Enter key
	await delayRandom(1000, 2000); //wait for a random amount of time
	for (let i = 0; i < 8; i++) { //loop 8 times
		await page.keyboard.press('Tab'); //press the Tab key
		await delayRandom(300, 600); //wait for a random amount of time
	}
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.type(lines[3], {delay: 150}); //type the third line of the description with a delay between keystrokes
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.click('#next-button'); //click the "Next" button
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.click('#next-button'); //click the "Next" button again
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.click('#next-button'); //click the "Next" button a third time
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.click('#offRadio'); //click the "Not made for kids" radio button
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.press('Tab'); //press the Tab key
	await delayRandom(1000, 2000); //wait for a random amount of time
	await page.keyboard.press('ArrowUp'); //press the Up Arrow key
	await delayRandom(15000, 20000); //wait for a random amount of time
	await page.click('#done-button');
	await delayRandom(15000, 20000);
	// At this point, the video should be uploaded. The following code navigates to the newly uploaded video's page and leaves a comment.
	// Get the URL of the newly uploaded video
	const element = await page.$('#share-url');
	const share = await page.evaluate(el => el.innerHTML, element);
	await page.goto(share);
    await delayRandom(10000, 15000);
	// Click the "Comments" button to expand the comments section
	await page.click('#comments-button');
	await delayRandom(5000, 10000);
	// Press the "Tab" key several times to navigate to the comment text box
	await page.keyboard.press('Tab');
	await delayRandom(1000, 2000);
	await page.keyboard.press('Tab');
	await delayRandom(1000, 2000);
	await page.keyboard.press('Tab');
	await delayRandom(1000, 2000);
	// Type the comment text into the text box
	await page.keyboard.type('Special prize for you: cpalinkhere', {delay: 150});
	await delayRandom(1000, 2000);
	// Click the "Submit" button to post the comment
	await page.click('#submit-button');
	await delayRandom(15000, 20000);
	// Print a message to indicate that the upload and comment posting are complete, and exit the script
	console.log('Upload completed')
	process.exit();
})
.catch(function(error) {
	console.error(error);
	//process.exit(); https://cracked.io/Evil-Corporation
});