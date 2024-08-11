// src/components/Board.js
import React from 'react';
import Tile from './Tile';
import '../styles.css';

const boardLayout = [
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
];

function Board({ onChoose, placedTiles }) {
  let tileIndex = 0;
  return (
    <div className="BoardContainer">
      {boardLayout.flat().map((cell, index) => {
        if (!cell) {
          return <div key={index}></div>;
        }
        tileIndex++;
        return (
          <div className="HexCell" key={index}>
            <Tile
              index={tileIndex}
              values={placedTiles[tileIndex - 1]}
              onClick={onChoose} // Example values
            />
          </div>
        );
      })}
    </div>
  );
}

export default Board;
