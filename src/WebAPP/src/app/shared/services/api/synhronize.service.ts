import { Injectable } from "@angular/core";
import { HttpService } from "../core/http.service";
import { BaseService } from "../core/base.service";
import { ClientConfigurationService } from "../core/client-configuration.service";
import { ServiceType } from "../core/serviceType";
import { MuseumTableModel } from "../../models/museumTable.model";

@Injectable()
export class SynhronizeService extends BaseService<any> {
  constructor(
    httpService: HttpService,
    configService: ClientConfigurationService) {
    super(httpService, 'synchronize', configService, MuseumTableModel, ServiceType.route);
  }
}
