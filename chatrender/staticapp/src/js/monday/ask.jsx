import React from 'react';

const Ask = (props) => {
  return props.live ? (
    <section className='ask'>
      Have a question?
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
    </section>
  ) : null;
};

export default Ask;
