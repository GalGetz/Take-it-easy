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

function Board({ title, onChoose, placedTiles, loaderTurn }) {
  let tileIndex = 0;
  return (
    <Box align="center">
      <Typography variant="h5">{title}</Typography>
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
                onClick={loaderTurn ? undefined : onChoose}
              />
            </div>
          );
        })}
      </div>
    </Box>
  );
}

export default Board;
