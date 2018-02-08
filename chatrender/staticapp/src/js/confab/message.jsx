import React from 'react';
import marked from 'marked';
import twemoji from 'twemoji';

import Byline from './byline';
import Reaction from './reaction';
import Ad from './cubeAd';

marked.setOptions({ smartypants: true });

const Message = (props) => {
  const reactions = props.message.reactions.map(r => (
    <Reaction
      reaction={r.reaction}
      user={props.users[r.user]}
    />
  ));

  let ad;
  switch (props.index) {
    case 6:
      ad = (<Ad num='06' />);
      break;
    case 12:
      ad = (<Ad num='07' />);
      break;
    case 18:
      ad = (<Ad num='08' />);
      break;
    default:
      break;
  }

  return (
    <div>
      {ad}
      <div className='message'>
        <Byline author={props.user} timestamp={props.message.timestamp} />
        <div className='content clearfix'>
          <div dangerouslySetInnerHTML={{
            __html: twemoji.parse(marked(props.message.content)),
          }} />
        </div>
        <div className='reactions-drawer'>
          {reactions}
        </div>
      </div>
    </div>
  );
};

export default Message;
