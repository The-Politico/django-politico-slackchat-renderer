import React from 'react';

const Ad = (props) => (
  <div className='content-group ad'>
    <p>Advertisement</p>
    <div
      className='ad-slot flex horizontal'
      id={`pol-${props.num}`}
    />
  </div>
);

export default Ad;
