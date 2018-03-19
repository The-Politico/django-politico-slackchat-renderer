import React from 'react';

const Image = (props) => (
  <div className='attachment video'>
    <div dangerouslySetInnerHTML={{
      __html: props.attachment.video_html.replace(
        'autoplay=1',
        'autoplay=0&fs=0&modestbranding=1&rel=0&showinfo=0'
      ),
    }} />
  </div>
);

export default Image;
