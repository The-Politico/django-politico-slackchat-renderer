import React from 'react';
import Message from './message';

const channelURI = document.getElementsByName('channel-uri')[0].value;

console.log(`${channelURI}/`);

class Blog extends React.Component {
  constructor (props) {
    super(props);
    this.state = { chat: [], };
    this.fetchChat = this.fetchChat.bind(this);
  }

  componentDidMount () {
    setInterval(this.fetchChat, 2500);
  }

  fetchChat () {
    fetch(`${channelURI}/`)
      .then(response => response.json())
      .then(data => {
        this.setState({ chat: data, });
      })
      .catch(e => console.log('API error: ', e));
  }

  render () {
    if (!this.state.chat.messages) return null;
    const users = this.state.chat.users;
    const messages = this.state.chat.messages.map(m => (
      <Message
        message={m}
        user={users[m.user]}
        users={users}
        key={m.id}
      />
    ));

    return (
      <div>
        <div>Component</div>
        <div className='chat-well'>
          {messages}
        </div>
      </div>
    );
  }
}

export default Blog;
