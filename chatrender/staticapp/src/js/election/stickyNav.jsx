import React from 'react';
import throttle from 'lodash/throttle';

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
    const waypoint = document.getElementById('introduction');
    const position = this.getOffset(waypoint);

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
          <div className='title'>
            <div className='logo'>
              <span className='icon icon-politico' />
              <span className='icon-text'>POLITICO</span>
              <span className='elex-tag'> Elections</span>
            </div>
            <div className='page-title'>
              <h2>Live Analysis</h2>
            </div>
          </div>
        </div>
      </div>
    );
  }
};

export default StickyHeader;
