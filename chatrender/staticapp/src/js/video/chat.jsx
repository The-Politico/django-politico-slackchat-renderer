import React from 'react';
import Message from './message';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import { faArrowUp } from '@fortawesome/fontawesome-free-solid';
import { scroller, Element } from 'react-scroll';
import sortBy from 'lodash/sortBy';
import Video from './video';
import Sticky from 'react-stickynode';

const channelURI = document.getElementsByName('channel-uri')[0].value;

class Chat extends React.Component {
  constructor (props) {
    super(props);
    this.state = { chat: [] };
    this.fetchChat = this.fetchChat.bind(this);
  }

  componentDidMount () {
    this.fetchChat();

    if (this.state.chat.live) {
      setTimeout(this.fetchChat, 2500);
    }
  }

  componentDidUpdate () {
    if (this.state.chat.live) {
      setTimeout(this.fetchChat, 2500);
    } else {
      setTimeout(this.fetchChat, 15000);
    }

    if (window.twttr) window.twttr.widgets.load(document.getElementById('blog'));
  }

  fetchChat () {
    fetch(`${channelURI}`)
      .then(response => response.json())
      .then(data => {
        this.setState({ chat: data });
      })
      .catch(e => console.log('API error: ', e));
  }

  render () {
    const chat = this.state.chat;
    if (!chat.messages) return null;
    const users = chat.users;
    const messages = sortBy(chat.messages, [d => d.timestamp]).map((m, i) => (
      <Message
        message={m}
        user={users[m.user]}
        users={users}
        key={m.id}
        index={i}
      />
    ));

    return (
      <div>
        <Sticky
          top={0}
          bottomBoundry='chat-well'
        >
          <Video />
        </Sticky>
        <Element name='chatTop' />
        <div className='chat-well' id='chat-well'>
          {messages}
          <Element name='chatBottom' />
          <div className='bottom-bumper'>
            <div
              id='loader'
              className={chat.live ? 'live' : ''}
            >
              <span className='dot' />
              <span className='dot' />
              <span className='dot' />
            </div>
            <button
              onClick={() => {
                scroller.scrollTo('chatTop', {
                  offset: -150,
                  smooth: true,
                  duration: 250,
                });
              }}
            >
              <FontAwesomeIcon icon={faArrowUp} />
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default Chat;
