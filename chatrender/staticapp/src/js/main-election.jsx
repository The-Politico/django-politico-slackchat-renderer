import React from 'react';
import ReactDOM from 'react-dom';

import './common/share';

import 'politico-style/scss/elections/states/main.scss';
import '../scss/election/main.scss';

import Chat from './election/chat.jsx';

ReactDOM.render(<Chat />, document.getElementById('blog'));
