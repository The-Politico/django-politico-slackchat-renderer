import React from 'react';
import { Twemoji } from 'react-emoji-render';
import ReactTooltip from 'react-tooltip';

const Reaction = (props) => (
  <div className='reaction'>
    <ReactTooltip
      class='reaction-tooltip'
      place='top'
      offset={{right: '15px', bottom: '7px'}}
      effect='solid'
      getContent={() => (
        <img
          className='reaction-tooltip-image'
          src={'https://upload.wikimedia.org/wikipedia/commons/b/bb/Tibur%C3%B3n.jpg'}
        />)}
    />
    <Twemoji
      data-tip
      text={`:${props.reaction}:`}
    />
  </div>
);

export default Reaction;
