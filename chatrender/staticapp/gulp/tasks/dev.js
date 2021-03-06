const app = require('../server/server.js');
const { exec } = require('child_process');
const { argv } = require('yargs');

const port = argv.port || 3000;
const proxy = argv.proxy || 8000;
const noPython = !!argv.nopython;

module.exports = () => {
  exec(`echo $PWD`, {
    cwd: './../../example/',
  });
  if (!noPython) exec(`pipenv run python manage.py migrate`, {
    cwd: './../../example/',
  });
  if (!noPython) exec(`pipenv run python manage.py runserver ${proxy}`, {
    cwd: './../../example/',
  });
  setTimeout(() => {
    app.startServer(port, proxy);
  }, 1000);
};
