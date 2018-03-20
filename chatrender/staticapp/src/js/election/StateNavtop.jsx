import React from 'react';
import states from './states.json';

const linkify = (state) => {
  const slug = state.toLowerCase().replace(' ', '-');
  return `https://www.politico.com/election-results/2018/${slug}`;
};

const StateNav = (props) => {
  const open = props.open ? 'open' : '';
  const lis = states.map(state => (
    <li><a href={linkify(state)}>{state}</a></li>
  ));
  return (
    <div className={`statenav-top ${open}`}>
      <ul>
        {lis}
      </ul>
    </div>
  );
};

export default StateNav;
