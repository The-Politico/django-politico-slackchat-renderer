import React from 'react';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import { faArrowDown } from '@fortawesome/fontawesome-free-solid';
import Scroll from 'react-scroll';

const scroll = Scroll.scroller;

const Video = () => (
  <div
    className='video-rail'
  >
    <div
      className='video-content clearfix'
    >
      <div
        className='video-box'
      >
        <div className='left' >
          <h6>Watch Live</h6>
        </div>
        <div className='right'>
          <iframe
            width='170'
            height='100'
            src='https://www.youtube.com/embed/Tch4v0L0GHA?rel=0&amp;showinfo=0&amp;controls=0'
            frameBorder='0'
            allow='autoplay; encrypted-media'
            playsinline='1'
            allowFullScreen
          />
        </div>
      </div>
      <div
        className='button-box'
      >
        <div className='top'>
          <h6>Latest</h6>
        </div>
        <div className='bottom'>
          <button
            onClick={() => {
              scroll.scrollTo('chatBottom', {
                offset: -350,
                smooth: true,
                duration: 250,
              });
            }}
          >
            <FontAwesomeIcon icon={faArrowDown} />
          </button>
        </div>
      </div>
    </div>
  </div>
);

export default Video;
