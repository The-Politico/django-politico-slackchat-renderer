import React from 'react';
import ReactDOM from 'react-dom';

import './common/share';

import 'politico-style/scss/base/main.scss';
// import '../scss/video/main.scss';

import Chat from './video/chat.jsx';

ReactDOM.render(<Chat />, document.getElementById('blog'));

window.$('#ask-politico').click((e) => {
  e.preventDefault();
  const status = encodeURIComponent('#AskPOLITICO');
  window.open(`https://twitter.com/intent/tweet?text=${status}`);
});
