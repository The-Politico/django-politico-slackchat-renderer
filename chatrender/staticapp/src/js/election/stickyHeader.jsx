import React from 'react';
import throttle from 'lodash/throttle';
import { scroller } from 'react-scroll';

class StickyHeader extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      sticky: false,
      navDropped: false,
    };
    this.setStickyNav = this.setStickyNav.bind(this);
  }
  componentDidMount () {
    window.onscroll = throttle(this.setStickyNav, 250);
  }
  getOffset (el) {
    const rect = el.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return rect.top + scrollTop;
  }
  setStickyNav () {
    const position = 150;
    if (window.scrollY > position && !this.state.sticky) {
      this.setState({
        sticky: true,
      });
    }
    if (window.scrollY < position && this.state.sticky) {
      this.setState({
        sticky: false,
        navDropped: false,
      });
    }
  }
  render () {
    const open = this.state.sticky ? 'open' : '';
    return (
      <div>
        <div className={`sticky-header ${open}`}>
          <div className='brand'>
            <h4>
              <b className='bt-icon bt-icon--politico' /> Elections
            </h4>
          </div>
          <div
            className='buttons'
            hidden={!this.props.live}
          >
            <button
              className='ask'
              onClick={(e) => {
                e.preventDefault();
                const status = encodeURIComponent('#AskPOLITICO');
                window.open(
                  `https://twitter.com/intent/tweet?text=${status}`,
                  '_blank',
                  'width=600,height=300'
                );
              }}
            >
              <b className='bt-icon bt-icon--twitter' /> #AskPOLITICO
            </button>
            <button
              className='latest'
              onClick={() => {
                scroller.scrollTo('chatBottom', {
                  offset: -350,
                  smooth: true,
                  duration: 250,
                });
              }}
            >Latest</button>
          </div>
        </div>
      </div>
    );
  }
};

export default StickyHeader;
