import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { Button, Collapse, Divider } from '@mui/material';

import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default class CreateMain extends React.Component {

    constructor(props) {
        super(props);
        this._handleTextFieldChange = this._handleTextFieldChange.bind(this);
        this._handleSubmit = this._handleSubmit.bind(this);
    }

    state = {
        topicKeywords: '',
        responseData: '',
        show: false,
    }

    _handleTextFieldChange(e) {
        const topicKeywords = e.target.value
        this.setState({ topicKeywords });
    }

    _handleSubmit(event) {
        event.preventDefault();
        // alert('Form submitted: ' + this.state.topicKeywords)

        axios.post('http://localhost:3001/episodes/generate/', {
            topicKeywords: this.state.topicKeywords
        })
            .then((response) => {
                this.setState({ responseData: response.data, show: true });
                // window.location.href = "http://localhost:3000/create-generated?topic=" + this.state.topicKeywords + "&res=" + response.data;
            });
    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <form onSubmit={this._handleSubmit}>
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
                            onChange={this._handleTextFieldChange}
                        />
                        <Button
                            variant="contained"
                            sx={{
                                width: "10vw",
                                minWidth: "100px",
                                maxWidth: "150px",
                                marginTop: "50px",
                                marginLeft: "45vw"
                            }}
                            type='submit'
                        >
                            Generate
                        </Button>
                    </form>
                    <Collapse in={this.state.show}>
                        <Divider sx={{
                            width: "80vw",
                            marginTop: "50px",
                            marginLeft: "10vw",
                            fontSize: "18px"
                        }}>
                            Output
                        </Divider>
                        <TextField
                            id="filled-multiline-static"
                            multiline
                            rows={4}
                            defaultValue={this.state.responseData}
                            variant="filled"
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                marginTop: "50px",
                                marginLeft: "30vw"
                            }}
                            InputProps={{
                                readOnly: true,
                            }}
                        />
                        <Button
                            variant="contained"
                            sx={{
                                width: "10vw",
                                minWidth: "100px",
                                maxWidth: "150px",
                                marginTop: "50px",
                                marginLeft: "45vw"
                            }}
                        >
                            Upload
                        </Button>
                    </Collapse>
                </main>
                {/* Footer */}
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
                {/* End footer */}
            </ThemeProvider >
        );
    }
}