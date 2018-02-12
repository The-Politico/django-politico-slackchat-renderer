import React from 'react';
import ellipsize from 'ellipsize';

const Link = (props) => {
  const serviceIcon = props.attachment.service_icon
    ? (<img src={props.attachment.service_icon} />) : null;

  return props.attachment.image_url ? (
    <div className='attachment link'>
      <a href={props.attachment.title_link} target='_blank'>
        <div className='clearfix'>
          <div className='column half title'>
            <div className='source'>
              <p>
                {serviceIcon} {props.attachment.service_name}
              </p>
            </div>
            <h5>{props.attachment.title}</h5>
            <p>{ellipsize(props.attachment.text, 140)}</p>
          </div>
          <div className='column half image'>
            <figure>
              <img src={props.attachment.image_url} />
            </figure>
          </div>
        </div>

      </a>
    </div>
  ) : (
    <div className='attachment link'>
      <a href={props.attachment.title_link} target='_blank'>
        <div className='column full title'>
          <div className='source'>
            <p>
              <img src={props.attachment.service_icon} /> {props.attachment.service_name}
            </p>
          </div>
          <h5>{props.attachment.title}</h5>
          <p>{ellipsize(props.attachment.text, 180)}</p>
        </div>
      </a>
    </div>
  );
};

export default Link;
