import React from 'react';
import Message from './message';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import { faBolt, faArrowDown, faArrowUp } from '@fortawesome/fontawesome-free-solid';
import Sticky from 'react-stickynode';
import { animateScroll, Element } from 'react-scroll';

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

    window.twttr.widgets.load(document.getElementById('blog'));
  }

  fetchChat () {
    console.log('polls');
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
    const messages = chat.messages.map((m, i) => (
      <Message
        message={m}
        user={users[m.user]}
        users={users}
        key={m.id}
        index={i}
      />
    ));

    const live = chat.live ? (
      <Sticky enabled top={0} innerZ={200} >
        <div className='header'>
          <b className='icon icon-politico' /> <FontAwesomeIcon icon={faBolt} /> Live
          <button
            onClick={() => {
              animateScroll.scrollToBottom({
                isDynamic: true,
              });
            }}
          ><FontAwesomeIcon icon={faArrowDown} /></button>
        </div>
      </Sticky>
    ) : (
      <Sticky enabled top={0} innerZ={200} >
        <div className='header'>
          <b className='icon icon-politico' />
        </div>
      </Sticky>
    );

    return (
      <div>
        <Element name='chatTop' />
        <div className='chat-well'>
          {live}
          {messages}
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
                animateScroll.scrollToTop();
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
