// src/components/Board.js
import React from 'react';
// import styled from 'styled-components';
import Tile from './Tile';
import '../styles.css';


// const BoardContainer = styled.div`
//   display: grid;
//   grid-template-columns: repeat(5, 80px);
//   grid-template-rows: repeat(9, 40px);
//   width: 420px;
//   height: 400px;
//   margin-bottom: 50px;
//   align: center;
// `;

// const HexCell = styled.div`
//   width: 130%;
//   height: 190%;
//   display: flex;
//   justify-content: center;
//   align-items: center;
// `;

const boardLayout = [
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0]
];

function Board({onChoose, placedTiles}) {

  let tileIndex = 0;
  return (
    <div className="BoardContainer">
      {boardLayout.flat().map((cell, index) => {
        if (!cell){
          return (<div key={index}>
          </div>);
        }
        tileIndex++;
        return (
        <div className="HexCell" key={index} >
            <Tile 
              index={tileIndex}
              values={placedTiles[tileIndex - 1]} 
              onClick={onChoose} // Example values
            />
        </div>
      );})}
    </div>
  );
}

export default Board;