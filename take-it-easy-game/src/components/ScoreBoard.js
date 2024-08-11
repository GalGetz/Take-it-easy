// src/components/ScoreBoard.js
import React from 'react';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import { CardContent, CardHeader } from '@mui/material';


function ScoreBoard() {
  return (
    <Card raised variant="outlined" sx={{textAlign: "center",width: "150px"}} >
      <CardHeader title="Score"/>
      <CardContent>
        <Typography variant="body1">
            10
        </Typography>
      </CardContent>
    </Card>
  );
}

export default ScoreBoard;