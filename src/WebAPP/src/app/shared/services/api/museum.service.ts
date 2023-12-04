import { Injectable } from "@angular/core";
import { HttpService } from "../core/http.service";
import { BaseService } from "../core/base.service";
import { ClientConfigurationService } from "../core/client-configuration.service";
import { ServiceType } from "../core/serviceType";
import { UserInfoModel } from "../../models/userInfo.model";
import { MuseumModel } from "../../models/museum.model";

@Injectable()
export class MuseumService extends BaseService<any> {
  constructor(
    httpService: HttpService,
    configService: ClientConfigurationService) {
    super(httpService, 'museum', configService, MuseumModel, ServiceType.route);
  }
}
