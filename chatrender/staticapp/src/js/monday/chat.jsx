import React from 'react';
import { scroller, Element } from 'react-scroll';
import sortBy from 'lodash/sortBy';
import includes from 'lodash/includes';
import StickyHeader from './stickyHeader';
import Ask from './ask';

import MessageDefault from './messages/default';
import MessageQuestion from './messages/question';

const channelURI = document.getElementsByName('channel-uri')[0].value;

class Chat extends React.Component {
  constructor (props) {
    super(props);
    this.state = { chat: {} };
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
    const messages = sortBy(chat.messages, [d => d.timestamp]).map((m, i) => {
      if (includes(m.args, 'question')) {
        return (
          <MessageQuestion
            message={m}
            user={users[m.user]}
            users={users}
            key={m.id}
            index={i}
            live={this.state.chat.live}
          />
        );
      } else {
        return (
          <MessageDefault
            message={m}
            user={users[m.user]}
            users={users}
            key={m.id}
            index={i}
            live={this.state.chat.live}
          />
        );
      }
    });

    return (
      <div>
        <StickyHeader live={this.state.chat.live} />
        <Ask live={this.state.chat.live} />
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
              Top
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default Chat;
