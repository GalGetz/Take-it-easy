import React from 'react';
import '../styles.css';

const colors = {
  1: '#fe8b34', // Red
  2: '#23d72c', // Green
  3: '#3357ff', // Blue
  4: '#ff33a8', // Pink
  5: '#cd90eb', // Cyan
  6: '#ffbd33', // Orange
  7: '#bd33ff', // Purple
  8: '#ff3333', // Dark Red
  9: '#07ede8', // Mint
};

function Tile({ index, values, onClick, isPicker }) {
  const onClickPlace = (index) => {
    if (values) {
      return;
    }
    onClick(index);
  };

  return (
    <div
      className={`${isPicker || values ? 'Picker' : 'TileContainer'}`}
      onClick={() => onClickPlace(index - 1)}
    >
      {values && (
        <>
          <div
            className="NumberTop"
            style={{ '--color-top': colors[values[0]] }}
          >
            {values[0]}
          </div>
          <div
            className="NumberLeft"
            style={{ '--color-left': colors[values[1]] }}
          >
            {values[1]}
          </div>
          <div
            className="NumberRight"
            style={{ '--color-right': colors[values[2]] }}
          >
            {values[2]}
          </div>
        </>
      )}
    </div>
  );
}

export default Tile;
