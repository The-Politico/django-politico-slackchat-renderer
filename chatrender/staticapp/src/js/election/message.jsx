import React from 'react';
import marked from 'marked';
import twemoji from 'twemoji';

import Byline from './byline';
import Reaction from './reaction';
import Ad from './cubeAd';
import LinkAttachment from './attachments/link';
import ImageAttachment from './attachments/image';
import VideoAttachment from './attachments/video';

marked.setOptions({ smartypants: true });

const Message = (props) => {
  const message = props.message;

  const reactions = message.reactions
    ? message.reactions.map(r => (
      <Reaction
        reaction={r.reaction}
        usertimestamp={`${r.user}${r.timestamp}`}
        user={props.users[r.user]}
        key={`${r.user}${r.timestamp}`}
      />
    )) : null;

  let ad;
  switch (props.index) {
    case 10:
      ad = (<Ad num='06' />);
      break;
    case 20:
      ad = (<Ad num='07' />);
      break;
    case 30:
      ad = (<Ad num='08' />);
      break;
    case 40:
      ad = (<Ad num='09' />);
      break;
    default:
      break;
  }

  const attachment = message.attachments ? message.attachments[0] : null;

  let Attachment;

  if (attachment && attachment.video_html) {
    if (attachment.service_name === 'YouTube') Attachment = (<VideoAttachment attachment={attachment} />);
  } else if (attachment && attachment.title_link) {
    Attachment = (<LinkAttachment attachment={attachment} />);
  } else if (
    attachment && attachment.image_url &&
    attachment.service_name !== 'twitter'
  ) {
    Attachment = (<ImageAttachment attachment={attachment} />);
  }

  return (
    <div>
      {ad}
      <div className='message'>
        <Byline author={props.user} timestamp={message.timestamp} />
        <div className='content clearfix'>
          <div dangerouslySetInnerHTML={{
            __html: message.content
              ? twemoji.parse(
                marked(message.content.replace(/&gt;+/g, '>'))
              ) : '',
          }} />
        </div>
        <div className='reactions-drawer'>
          {reactions}
        </div>
        {Attachment}
      </div>
    </div>
  );
};

export default Message;
