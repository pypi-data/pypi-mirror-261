import json
import uuid
from typing import BinaryIO

from rich import print

from doipy.config import settings
from doipy.fdo_config import FDO_Profile_Ref, FDO_Type_Ref
from doipy.socket_utils import create_socket, send_message, finalize_socket, read_response


def create_fdo(data_ref: str, md_ref: str, client_id: str, password: str):
    operation_id = '0.DOIP/Op.Create'
    do_type = 'FDO'
    with create_socket() as ssl_sock:
        message = {
            'clientId': client_id,
            'targetId': f'{settings.prefix}/service',
            'operationId': operation_id,
            'authentication': {
                'password': password
            }
        }
        send_message(message, ssl_sock)
        message = {
            'type': do_type,
            'attributes': {
                'content': {
                    'id': '',
                    'FDO_Profile_Ref': FDO_Profile_Ref,
                    'FDO_Type_Ref': FDO_Type_Ref,
                    'FDO_Data_Refs': [data_ref],
                    'FDO_MD_Refs': [md_ref]
                }
            }
        }
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        read_response(ssl_sock)


def create(do_type: str, files: list[BinaryIO], md_file: str, client_id: str, password: str):
    operation_id = '0.DOIP/Op.Create'
    if do_type is None:
        return
    with create_socket() as ssl_sock:
        message = {
            'clientId': client_id,
            'targetId': f'{settings.prefix}/service',
            'operationId': operation_id,
            'authentication': {
                'password': password
            }
        }
        send_message(message, ssl_sock)

        if do_type == 'Document':
            message = {
                'type': do_type,
                'attributes': {
                    'content': {
                        'id': ''
                    }
                }
            }
            my_uuids = {}
            elements = []
            for file in files:
                filename = file.name
                my_uuids[filename] = str(uuid.uuid4())
                elements.append(
                    {
                        'id': my_uuids[filename],
                        'type': 'text/plain',
                        'attributes': {
                            'filename': filename
                        }
                    }
                )
                message['elements'] = elements

            if md_file is not None:
                with open(md_file, 'r') as md_f:
                    data = json.load(md_f)
                    for key in data:
                        message['attributes']['content'][key] = data[key]
            send_message(message, ssl_sock)

            for filename in my_uuids:
                message = {'id': my_uuids[filename]}
                send_message(message, ssl_sock)

                buffer_size = 1024
                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(buffer_size)
                        if not bytes_read:
                            break
                        ssl_sock.sendall(bytes_read)

                finalize_socket(ssl_sock)

            finalize_socket(ssl_sock)
            reply = json.loads(read_response(ssl_sock))
            if reply['status'] == '0.DOIP/Status.102':
                print('Authentication failed')
                return
            # Next step: update the DO to put the correct metadata
            # update(reply['output']['id'], client_id, password, do_type)


def update(target_id: str, client_id: str, password: str, do_type: str):
    operation_id = '0.DOIP/Op.Update'

    with create_socket() as ssl_sock:
        message = {
            'clientId': client_id,
            'targetId': target_id,
            'operationId': operation_id,
            'authentication': {
                'password': password
            }
        }
        send_message(message, ssl_sock)
        string1 = f'https://cordra.testbed.pid.gwdg.de/objects/{target_id}?payload=file'
        string2 = f'https://cordra.testbed.pid.gwdg.de/objects/{target_id}'
        message = {
            'type': do_type,
            'attributes': {
                'content': {
                    'id': '',
                    'Payload': string1,
                    'Metadata': string2
                }
            }
        }
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        read_response(ssl_sock)


def search(query: str = 'type:Document', username: str = None, password: str = None):
    operation_id = '0.DOIP/Op.Search'
    message = {
        'targetId': f'{settings.prefix}/service',
        'operationId': operation_id,
        'attributes': {
            'query': query
        }
    }
    if username and password:
        message['authentication'] = {'username': username, 'password': password}

    with create_socket() as ssl_sock:
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        read_response(ssl_sock)


def hello(username: str, password: str):
    operation_id = '0.DOIP/Op.Hello'

    message = {
        'targetId': f'{settings.prefix}/service',
        'operationId': operation_id,
        'authentication': {
            'username': username, 'password': password
        }
    }

    with create_socket() as ssl_sock:
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        read_response(ssl_sock)


def list_operations(target_id: str, client_id: str, password: str):
    operation_id = '0.DOIP/Op.ListOperations'
    message = {'operationId': operation_id}

    if target_id is None:
        message['targetId'] = f'{settings.prefix}/service'
    else:
        message['targetId'] = target_id

    if client_id is not None and password is not None:
        message['clientId'] = client_id
        message['authentication'] = {'password': password}

    with create_socket() as ssl_sock:
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        read_response(ssl_sock)
