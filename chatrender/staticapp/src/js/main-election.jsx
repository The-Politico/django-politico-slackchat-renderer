import React from 'react';
import ReactDOM from 'react-dom';

import './common/share';

import 'politico-style/scss/elections/states/main.scss';
// import '../scss/election/main.scss';

import Chat from './election/chat.jsx';

ReactDOM.render(<Chat />, document.getElementById('blog'));

window.$('#ask-politico').click((e) => {
  e.preventDefault();
  const status = encodeURIComponent('#AskPOLITICO');
  window.open(`https://twitter.com/intent/tweet?text=${status}`);
});
