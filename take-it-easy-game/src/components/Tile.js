import React from 'react';
import '../styles.css';

const colors = {
  1: '#ff5733', // Red
  2: '#33ff57', // Green
  3: '#3357ff', // Blue
  4: '#ff33a8', // Pink
  5: '#33fff7', // Cyan
  6: '#ffbd33', // Orange
  7: '#bd33ff', // Purple
  8: '#ff3333', // Dark Red
  9: '#33ffbd', // Mint
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
