import React from 'react';
import { Emojione, } from 'react-emoji-render';

const Reaction = (props) => (
  <div className='reaction'>
    <Emojione text={`:${props.reaction}:`} />
  </div>
);

export default Reaction;
