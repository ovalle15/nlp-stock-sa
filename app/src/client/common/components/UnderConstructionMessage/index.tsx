import React from 'react';
import { Alert, AlertIcon, AlertTitle } from '@chakra-ui/react';

function UnderConstructionMessage({ ...props }: typeof Alert) {
    return (
        <Alert status="warning" variant="left-accent" {...props}>
            <AlertIcon />
            <AlertTitle>{`🚧 Under Construction... 🤓 🚧`}</AlertTitle>
        </Alert>
    );
}

export default UnderConstructionMessage;
