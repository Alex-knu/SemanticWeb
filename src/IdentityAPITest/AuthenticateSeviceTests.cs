using NUnit.Framework;
using Moq;
using Microsoft.Extensions.Configuration;
using System.Threading.Tasks;
using IdentityApi.Core.Services;
using IdentityApi.Core.Models;
using Microsoft.AspNetCore.Identity;
using System.Security.Claims;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System;
using System.Linq;

namespace IdentityAPITest;

public class AuthenticateSeviceTests
{
    private AuthenticateSevice _authenticateService;
    private Mock<IConfiguration> _configurationMock;

    [SetUp]
    public void Setup()
    {
        // Arrange
        var roles = new List<IdentityRole>
            {
                new IdentityRole("Admin"),
                new IdentityRole("User")
            };

        var mockRoleStore = new Mock<IRoleStore<IdentityRole>>();
        var roleManagerMock = new Mock<RoleManager<IdentityRole>>(mockRoleStore.Object, null, null, null, null);
        roleManagerMock.Setup(rm => rm.Roles).Returns(roles.AsQueryable());

        var userStoreMock = new Mock<IUserStore<IdentityUser>>();
        var userManagerMock = new Mock<UserManager<IdentityUser>>(userStoreMock.Object, null, null, null, null, null, null, null, null);
        userManagerMock.Setup(x => x.FindByNameAsync(It.IsAny<string>()))
                       .ReturnsAsync(new IdentityUser { UserName = "ValidUsername", Id = "UserId" });
        userManagerMock.Setup(x => x.CheckPasswordAsync(It.IsAny<IdentityUser>(), It.IsAny<string>()))
                       .ReturnsAsync(false);
        userManagerMock.Setup(x => x.CreateAsync(It.IsAny<IdentityUser>(), It.IsAny<string>())).ReturnsAsync(new IdentityResult());

        _configurationMock = new Mock<IConfiguration>();
        _configurationMock.Setup(x => x["JWT:Secret"]).Returns("your_secret_key");
        _configurationMock.Setup(x => x["JWT:ValidIssuer"]).Returns("your_issuer");
        _configurationMock.Setup(x => x["JWT:ValidAudience"]).Returns("your_audience");


        _authenticateService = new AuthenticateSevice(userManagerMock.Object, roleManagerMock.Object, _configurationMock.Object);
    }

    [Test]
    public async Task Login_ValidLoginInfo_WrongPasswordAsync()
    {
        // Arrange
        var validLoginModel = new LoginModel { Username = "ValidUsername", Password = "ValidPassword" };

        string expectedException = string.Empty;

        try
        {
            await _authenticateService.Login(validLoginModel);
        }
        catch (Exception ex)
        {
            expectedException = ex.Message;
        }

        Assert.AreEqual(expectedException, "Wrong user credentials!");
    }

    [Test]
    public async Task IsUserExistByName_FindUser_ExsistUser()
    {
        // Arrange
        var validLoginModel = new LoginModel { Username = "ValidUsername", Password = "ValidPassword" };

        string expectedException = string.Empty;

        try
        {
            await _authenticateService.IsUserExistByName(validLoginModel.Username);
        }
        catch (Exception ex)
        {
            expectedException = ex.Message;
        }

        Assert.AreEqual(expectedException, "User already exists!");
    }


    [Test]
    public void GetToken_ReturnsJwtSecurityToken()
    {
        // Arrange
        var authClaims = new List<Claim>
            {
                new Claim("UserIdentifier", Guid.NewGuid().ToString()),
                new Claim("UserName", "Test"),
                new Claim("Jti", Guid.NewGuid().ToString()),
            };

        // Act
        var result = _authenticateService.GetToken(authClaims);

        // Assert
        Assert.IsNotNull(result);
        Assert.IsInstanceOf<JwtSecurityToken>(result);
    }
}