import React from 'react';
import { scroller } from 'react-scroll';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import faPointDown from '@fortawesome/fontawesome-free-solid/faHandPointDown';

class Bug extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      topThreshold: false,
      bottomThreshold: false,
    };

    this.observeBottom = this.observeBottom.bind(this);
    this.observeTop = this.observeTop.bind(this);
  }

  componentDidMount () {
    const options = {
      rootMargin: '0px',
      threshold: 0,
    };

    this.bottomObserver = new IntersectionObserver(this.observeBottom, options);
    this.topObserver = new IntersectionObserver(this.observeTop, options);

    this.bottomTarget = document.querySelector('div[name="chatBottom"]');
    this.bottomObserver.observe(this.bottomTarget);

    this.topTarget = document.querySelector('div[name="chatTop"]');
    this.topObserver.observe(this.topTarget);
  }

  observeBottom (e) {
    const intersecting = e[0].isIntersecting;
    const { bottom } = this.bottomTarget.getBoundingClientRect();
    if (bottom < 0) return;
    this.setState({
      bottomThreshold: !intersecting,
    });
  }

  observeTop (e) {
    const intersecting = e[0].isIntersecting;
    const { top } = this.topTarget.getBoundingClientRect();
    if (window.pageYOffset < top) return;
    this.setState({
      topThreshold: !intersecting,
    });
  }

  render () {
    if (!this.props.live) return null;

    const className = this.state.bottomThreshold && this.state.topThreshold
      ? 'bug active' : 'bug';

    return (
      <div
        className={className}
      >
        <button
          onClick={() => {
            scroller.scrollTo('chatBottom', {
              offset: -350,
              smooth: true,
              duration: 250,
            });
          }}
        >
          <FontAwesomeIcon icon={faPointDown} />
        </button>
      </div>
    );
  }
}

export default Bug;
