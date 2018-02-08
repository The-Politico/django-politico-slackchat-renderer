import React from 'react';
import moment from 'moment-timezone';

moment.updateLocale('en', {
  meridiem: function (hour, minute, isLowercase) {
    if (hour < 12) {
      return 'a.m.';
    } else {
      return 'p.m.';
    }
  },
});

const Byline = (props) => (
  <div className='byline clearfix'>
    <div className='byline-pic'>
      <figure>
        <img src='https://upload.wikimedia.org/wikipedia/commons/b/bb/Tibur%C3%B3n.jpg' />
      </figure>
    </div>
    <div className='byline-identity'>
      <span className='name'>{props.author.first_name} {props.author.last_name}</span>
      <br /><span className='title'>{props.author.title}</span>
    </div>
    <div className='byline-timestamp'>
      {moment.tz(props.timestamp, 'America/New_York').format('h:mm a')}
    </div>
  </div>
);

export default Byline;
