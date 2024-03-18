import React from 'react';
import { Card, CardMedia, CssBaseline, Box } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { useSearchParams } from 'react-router-dom';

const defaultTheme = createTheme();

function ViewEpisodeMain() {
    const [queryParams] = useSearchParams();
    const title = queryParams.get("title");

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
                        image={`https://aipodcaststorage.blob.core.windows.net/podcast-media/${title}.mp4`}
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

export default ViewEpisodeMain;
