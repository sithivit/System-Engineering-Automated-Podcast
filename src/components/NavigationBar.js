import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';

export default function NavigationBar() {
    const navItems = ["home", "episodes", "create"]
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static" >
                <Toolbar sx={{ justifyContent: 'space-between' }}>
                    <Link to="/">
                        <img src="/logo.png" alt="logo" style={{ maxWidth: '200px' }} />
                    </Link>
                    <Typography variant="h6" sx={{ my: 2 }}>
                        <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
                            {navItems.map((item) => (
                                <Link to={"/" + item}>
                                    <Button key={item} sx={{
                                        color: '#fff',
                                        fontSize: "17px",
                                        marginLeft: "20px"
                                    }}>
                                        {item}
                                    </Button>
                                </Link>
                            ))}
                        </Box>
                    </Typography>
                    <Link to="/login">
                        <Button variant="contained" sx={{
                            backgroundColor: '#fff',
                            color: '#1976d2',
                            fontSize: "17px",
                            fontWeight: "bold",
                            marginLeft: "20px"
                        }}>
                            Login
                        </Button>
                    </Link>
                </Toolbar>
            </AppBar>
        </Box >
    );
}