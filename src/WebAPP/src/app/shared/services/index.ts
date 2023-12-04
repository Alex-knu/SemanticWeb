import { HttpService } from "./core/http.service";
import { ClientConfigurationService } from "./core/client-configuration.service";
import { ApiService } from "./api/api.service";
import { UserService } from "./api/user.service";
import { RoleService } from "./api/role.service";
import { MuseumService } from "./api/museum.service";
import { MuseumTableService } from "./api/museumTable.service";

export const services = [
  HttpService,
  ClientConfigurationService,
  ApiService,
  UserService,
  RoleService,
  MuseumService,
  MuseumTableService
]
