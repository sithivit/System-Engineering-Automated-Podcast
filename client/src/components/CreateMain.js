import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider, styled } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { Button, Collapse, Divider, Card, CardMedia, FormGroup, FormControlLabel, Checkbox, Stack, Typography, Switch } from '@mui/material';

import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

const AntSwitch = styled(Switch)(({ theme }) => ({
    width: 28,
    height: 16,
    padding: 0,
    display: 'flex',
    '&:active': {
        '& .MuiSwitch-thumb': {
            width: 15,
        },
        '& .MuiSwitch-switchBase.Mui-checked': {
            transform: 'translateX(9px)',
        },
    },
    '& .MuiSwitch-switchBase': {
        padding: 2,
        '&.Mui-checked': {
            transform: 'translateX(12px)',
            color: '#fff',
            '& + .MuiSwitch-track': {
                opacity: 1,
                backgroundColor: theme.palette.mode === 'dark' ? '#177ddc' : '#1890ff',
            },
        },
    },
    '& .MuiSwitch-thumb': {
        boxShadow: '0 2px 4px 0 rgb(0 35 11 / 20%)',
        width: 12,
        height: 12,
        borderRadius: 6,
        transition: theme.transitions.create(['width'], {
            duration: 200,
        }),
    },
    '& .MuiSwitch-track': {
        borderRadius: 16 / 2,
        opacity: 1,
        backgroundColor:
            theme.palette.mode === 'dark' ? 'rgba(255,255,255,.35)' : 'rgba(0,0,0,.25)',
        boxSizing: 'border-box',
    },
}));

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
        changed: false,
        isLocalModel: true,
        isOpenAI: false,
    }

    _handleTextFieldChange(e) {
        this.setState({ topicKeywords: e.target.value });
    }

    _handleSubmit(event) {
        event.preventDefault();
        this.setState({ changed: true });

        if (this.state.topicKeywords.trim() !== '') {
            axios.post('http://localhost:3001/episodes/generate/', {
                topicKeywords: this.state.topicKeywords
            })
                .then((response) => {
                    this.setState({ responseData: response.data, show: true });
                    // window.location.href = "http://localhost:3000/create-generated?topic=" + this.state.topicKeywords + "&res=" + response.data;
                });
        }


    }

    _handleCheckbox(e) {
        this.setState({ isOpenAI: e });
    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <form onSubmit={this._handleSubmit}>
                        <Stack
                            direction="row"
                            spacing={1}
                            alignItems="center"
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                marginTop: "50px",
                                marginLeft: "30vw"
                            }}
                        >
                            <Typography>Number of Guests: Single</Typography>
                            <AntSwitch defaultChecked inputProps={{ 'aria-label': 'ant design' }} />
                            <Typography>Multiple</Typography>
                        </Stack>
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
                                marginTop: "20px",
                                marginLeft: "30vw"
                            }}
                            onChange={this._handleTextFieldChange}
                            error={this.state.topicKeywords.trim() === "" && this.state.changed}
                            helperText={this.state.topicKeywords.trim() === "" && this.state.changed ? 'Field required!' : ' '}
                        />
                        <FormGroup
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                marginLeft: "30vw"
                            }}
                        >
                            <FormControlLabel
                                control={<Checkbox />}
                                checked={this.state.isLocalModel}
                                label="Local Model"
                                onClick={() => this.setState({ isLocalModel: !this.state.isLocalModel, isOpenAI: false })}
                            />
                            <FormControlLabel
                                control={<Checkbox />}
                                checked={this.state.isOpenAI}
                                label={"OpenAI"}
                                onClick={() => this.setState({ isOpenAI: !this.state.isOpenAI, isLocalModel: false })}
                            />
                            <Collapse in={this.state.isOpenAI}>
                                <TextField
                                    label="OpenAI API"
                                    defaultValue=''
                                    variant="filled"
                                    type='password'
                                    sx={{
                                        width: "40vw",
                                        maxWidth: '100%',
                                    }}
                                />
                            </Collapse>
                            {/* <FormControlLabel required control={<Checkbox />} label="Required" />
                            <FormControlLabel disabled control={<Checkbox />} label="Disabled" /> */}
                        </FormGroup>

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

                    {/* The part below is displayed after form submission */}
                    <Collapse in={this.state.show}>
                        <Divider sx={{
                            width: "80vw",
                            marginTop: "50px",
                            marginLeft: "10vw",
                            fontSize: "18px"
                        }}>
                            Output
                        </Divider>
                        <Box
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                mx: "30vw",
                                my: '50px',
                            }}
                        >
                            {this.state.responseData}
                        </Box>
                        <Card sx={{ width: '50vw', marginLeft: '25vw' }} >
                            <CardMedia
                                component='video'
                                image='https://srvcdn15.2convert.me/dl?hash=S61wRx5oRhsl49MKlNzq7ku7eIICJB6seE6VUht9sLO91USCeLpculJ4Mx8AJwtAbpATVwPSRCI0QmC0ElSHjSuknVLHmKMO1RLYG8qvik1aplw3lekeJO29J9wRgehtlv%2Bmckz%2B8J6Xn%2BOv4g4CxIbh3HAcWyPzy%2FAkbDsyXgsJufMRfOhxA2yaZvapu85oeEKfeD%2BaMrsdDl4BiQHlWRn8q7DbYvlxhMfWtyZmgQ5y3eIPFan7HIPsmcGByMrZJIsab01EEGG7xvJzxMUNYJTkaDoSab%2FPgSNclAJ2jsA%3D'
                                controls
                            />
                        </Card>
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