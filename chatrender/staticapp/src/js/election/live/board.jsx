import React from 'react';
import { scroller } from 'react-scroll';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import faPointDown from '@fortawesome/fontawesome-free-solid/faHandPointDown';

const Board = (props) => {
  return props.live ? (
    <section className='liveboard clearfix'>
      <div className='fifty'>
        <h4>
          This chat is <strong><b className='bt-icon bt-icon--circle-solid' />LIVE</strong>
        </h4>
        <h6>Catch up to the latest</h6>
      </div>
      <div className='fifty'>
        <button
          onClick={() => {
            scroller.scrollTo('chatBottom', {
              offset: -350,
              smooth: true,
              duration: 250,
            });
          }}
        >
          <FontAwesomeIcon icon={faPointDown} />
        </button>
      </div>
    </section>
  ) : null;
};

export default Board;
