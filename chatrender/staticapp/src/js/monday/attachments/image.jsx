import React from 'react';

const Image = (props) => (
  <div className='attachment image'>
    <figure>
      <img src={props.attachment.image_url} />
    </figure>
  </div>
);

export default Image;
