const fs = require('fs');
const logger = require('tracer').colorConsole();
const data = fs.readFileSync('file');
logger.log('1: ' + data.toString());

fs.readFile('file', function(err, docs, test) {
	if (err) {
		logger.trace('2: ' + err);
	}
	else {
		logger.debug('3: ' + docs);
	}
});
logger.warn('4: ' + 'Hai');

