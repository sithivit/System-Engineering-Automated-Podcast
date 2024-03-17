import * as React from 'react';
import { Card, CardMedia, CssBaseline, Box } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js'

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default class ViewEpisode extends React.Component {

    render() {
        return (
            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <Card sx={{
                        width: '50vw',
                        height: '28.125vw',
                        marginLeft: '25vw',
                        marginTop: '80px'
                    }} >
                        <CardMedia
                            component='video'
                            sx={{
                                height: '28.125vw',
                            }}
                            image='https://aipodcaststorage.blob.core.windows.net/podcast-media/sample.mp4'
                            controls
                        />
                    </Card>
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