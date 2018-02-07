import React from 'react';
import ReactDOM from 'react-dom';

import '../scss/blog/main.scss';

import Blog from './blog/blog.jsx';

const App = () => (
  <div>
    <h3>Test</h3>
    <Blog />
  </div>
);

ReactDOM.render(<App />, document.getElementById('blog'));
