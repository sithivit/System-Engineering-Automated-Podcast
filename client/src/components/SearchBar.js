import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function SearchBar() {
    return (
        <Box
            sx={{
                width: "60vw",
                maxWidth: '100%',
                marginTop: "50px",
                marginLeft: "20vw"
            }}
        >
            <TextField fullWidth label="Search episodes..." id="search" />
        </Box>
    );
}