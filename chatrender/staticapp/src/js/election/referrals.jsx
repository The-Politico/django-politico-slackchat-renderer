import React from 'react';
import {
  CSSTransition,
  TransitionGroup,
} from 'react-transition-group';

class Referrals extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      open: false,
    };
  }
  render () {
    const referralLinks = this.state.open ? this.props.links.map(d => (
      <CSSTransition
        key={d.link}
        timeout={0}
        classNames='fade'
      >
        <a key={d.link} href={d.link} target='_blank'>
          <button>
            {d.title}
          </button>
        </a>
      </CSSTransition>
    )) : null;
    return (
      <div className='referral'>
        <div>
          <TransitionGroup>
            {referralLinks}
          </TransitionGroup>
          <button
            onClick={() => { this.setState({ open: !this.state.open }); }}
          >
            <span
              hidden={!this.props.live}
            >Live</span> Results
          </button>
        </div>
      </div>
    );
  }
}

export default Referrals;
