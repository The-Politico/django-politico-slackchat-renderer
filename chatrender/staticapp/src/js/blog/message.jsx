import React from 'react';
import ReactMarkdown from 'react-markdown';

import Byline from './byline';
import Reaction from './reaction';

const Message = (props) => {
  const reactions = props.message.reactions.map(r => (
    <Reaction reaction={r.reaction} />
  ));
  return (
    <div className='message'>
      <div className='content'>
        <ReactMarkdown source={props.message.content} />
        <Byline author={props.user} />
        {reactions}
      </div>
    </div>
  );
};

export default Message;
