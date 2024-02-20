import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js'
import { Button, Divider } from '@mui/material';
import AudioPlayerSlider from './AudioPlayerSlider.js'

// import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default class CreateMain extends React.Component {
    state = {
        // episodes: []
    }

    componentDidMount() {
        // axios.get(`http://localhost:3001/episodes`)
        //     .then(res => {
        //         const episodes = res.data;
        //         this.setState({ episodes });
        //     })
    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <TextField
                        id="filled-multiline-static"
                        label="Topic Keywords"
                        multiline
                        rows={4}
                        defaultValue=""
                        variant="filled"
                        sx={{
                            width: "40vw",
                            maxWidth: '100%',
                            marginTop: "50px",
                            marginLeft: "30vw"
                        }}
                    />
                    <Button
                        variant="contained"
                        sx={{
                            width: "10vw",
                            minWidth: "100px",
                            marginTop: "50px",
                            marginLeft: "45vw"
                        }}
                    >
                        Generate
                    </Button>
                    <Divider sx={{
                        width: "80vw",
                        marginTop: "50px",
                        marginLeft: "10vw",
                        fontSize: "18px"
                    }}>
                        Output
                    </Divider>
                    <AudioPlayerSlider />
                </main>
                {/* Footer */}
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
                {/* End footer */}
            </ThemeProvider>
        );
    }
}