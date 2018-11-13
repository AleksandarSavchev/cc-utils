# Copyright (c) 2018 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed
# under the Apache Software License, v. 2 except as noted otherwise in the LICENSE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import abort

from flask_restful import (
    Resource,
    reqparse,
)


class GithubWebhook(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('X-GitHub-Event', type=str, location='headers')

    def post(self):
        args = self.parser.parse_args()
        event = args.get('X-GitHub-Event')
        if not event:
            abort(400, 'X-GitHub-Event must be set')

        if event in ():
            pass
        else:
            return f'event {event} ignored'
