// src/components/Board.js
import React from 'react';
import { Box, Typography } from '@mui/material';
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

function Board({ title, onChoose, placedTiles, loaderTurn, background }) {
  let tileIndex = 0;
  return (
    <Box align="center">
      <Typography variant="h5">{title}</Typography>
      <div
        className="BoardContainer"
        style={
          background !== undefined
            ? {
                background: background
                  ? 'rgba(144, 238, 144, 0.3)'
                  : 'rgba(251, 50, 50, 0.3)',
              }
            : {
                backgroundColor: '#e2e8e4',
              }
        }
      >
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
                onClick={loaderTurn ? () => {} : onChoose}
              />
            </div>
          );
        })}
      </div>
    </Box>
  );
}

export default Board;
