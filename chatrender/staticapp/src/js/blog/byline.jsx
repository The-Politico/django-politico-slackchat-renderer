import React from 'react';

const Byline = (props) => (
  <div className='byline'>
    <div>
      {props.author.first_name} {props.author.last_name}
    </div>
  </div>
);

export default Byline;
