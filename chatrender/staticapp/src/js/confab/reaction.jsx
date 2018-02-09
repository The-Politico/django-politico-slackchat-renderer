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
      id={props.usertimestamp}
      getContent={() => (
        <img
          className='reaction-tooltip-image'
          src={props.user.image}
        />)}
    />
    <Twemoji
      data-tip
      data-for={props.usertimestamp}
      text={`:${props.reaction}:`}
    />
  </div>
);

export default Reaction;
